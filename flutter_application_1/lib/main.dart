// 1. Import the necessary packages at the top
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io'; // To handle the image file

// 2. Define the main entry point of your Flutter app
void main() => runApp(MyApp());

// 3. The main app class that defines the basic structure (StatelessWidget in this case)
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Medication App',
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: ImagePickerWidget(),
      ),
    );
  }
}

// 4. Define the StatefulWidget that contains the image picker functionality
class ImagePickerWidget extends StatefulWidget {
  const ImagePickerWidget({super.key});

  @override
  _ImagePickerWidgetState createState() => _ImagePickerWidgetState();
}

// 5. Define the state class that will handle the camera logic and UI updates
class _ImagePickerWidgetState extends State<ImagePickerWidget> {
  File? _image;

  // Method to capture image from camera
  Future<void> _pickImage() async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.camera);

    if (pickedFile != null) {
      setState(() {
        _image = File(pickedFile.path); // Store the image file
      });
    } else {
      print('No image selected.');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Pick an Image'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _image == null
                ? const Text('No image selected.')
                : Image.file(_image!), // Display the image if available
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _pickImage, // Button to trigger image picking
              child: const Text('Capture Image'),
            ),
          ],
        ),
      ),
    );
  }
}