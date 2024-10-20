import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MediScanApp());
}

class MediScanApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MediScan',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: Homepage(),
    );
  }
}

class Homepage extends StatefulWidget {
  @override
  _HomepageState createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  final ImagePicker _picker = ImagePicker();

  Future<void> _openCamera(BuildContext context) async {
    final XFile? image = await _picker.pickImage(source: ImageSource.camera);
    if (image != null) {
      Map<String, String> resultData = await _uploadAndDetectText(File(image.path));

      Navigator.of(context).push(MaterialPageRoute(
        builder: (context) => ResultPage(
          detectedText: resultData['detected_text'] ?? 'No text detected',
          aiResponse: resultData['ai_response'] ?? 'No response from AI',
        ),
      ));
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('No photo taken.')),
      );
    }
  }

  Future<Map<String, String>> _uploadAndDetectText(File imageFile) async {
    try {
      var request = http.MultipartRequest(
        'POST',
        Uri.parse('http://<backend-url>/detect_text'), // Replace with your backend URL
      );
      request.files.add(await http.MultipartFile.fromPath('image', imageFile.path));

      var response = await request.send();
      if (response.statusCode == 200) {
        String result = await response.stream.bytesToString();
        Map<String, dynamic> jsonResult = json.decode(result);
        return {
          'detected_text': jsonResult['detected_text'],
          'ai_response': jsonResult['ai_response']
        };
      } else {
        return {'error': 'Error extracting text'};
      }
    } catch (e) {
      return {'error': 'Error: $e'};
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('MediScan'),
      ),
      backgroundColor: const Color.fromARGB(255, 76, 175, 152),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/BackgroundHomepage.png',
              width: 500,
              height: 500,
            ),
            SizedBox(height: 20),
            ElevatedButton.icon(
              onPressed: () {
                _openCamera(context);
              },
              icon: Image.asset(
                'assets/Camera_icon.png',
                width: 24,
                height: 24,
              ),
              label: Text('Open Camera'),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.white,
                foregroundColor: Colors.black,
                minimumSize: Size(500, 50),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton.icon(
              onPressed: () {
                Navigator.of(context).push(
                  MaterialPageRoute(builder: (context) => SettingsPage()),
                );
              },
              icon: Image.asset(
                'assets/Settings_icon.png',
                width: 24,
                height: 24,
              ),
              label: Text('Settings'),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.white,
                foregroundColor: Colors.black,
                minimumSize: Size(200, 50),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class ResultPage extends StatelessWidget {
  final String detectedText;
  final String aiResponse;

  ResultPage({
    required this.detectedText,
    required this.aiResponse,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('MediScan Result'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Detected Text: $detectedText'),
            SizedBox(height: 10),
            Text('AI Response: $aiResponse'),
          ],
        ),
      ),
    );
  }
}

class SettingsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Settings'),
      ),
      body: Center(
        child: Text('Settings Page'),
      ),
    );
  }
}
