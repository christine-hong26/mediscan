import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

void main() {
  runApp(DrugScannerApp());
}

class DrugScannerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(primarySwatch: Colors.green),
      home: SplashScreen(),
    );
  }
}

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Future.delayed(Duration(seconds: 2), () {
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: Text('Warning', style: TextStyle(fontSize: 24)),
          content: Text(
            'The provided information does not replace medical advice. Consult a doctor for professional advice.',
            style: TextStyle(fontSize: 18),
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushReplacement(
                    MaterialPageRoute(builder: (context) => SettingsPage()));
              },
              child: Text('OK', style: TextStyle(fontSize: 18)),
            ),
          ],
        ),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
            Text(
              'MediScan',
              style: TextStyle(
                fontSize: 32,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ],
        ),
      ),
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
      Navigator.of(context).push(MaterialPageRoute(
        builder: (context) => ResultPage(
          sex: 'Unknown',
          age: 'Unknown',
          weight: 'Unknown',
        ),
      ));
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('No photo taken.')),
      );
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

class SettingsPage extends StatefulWidget {
  @override
  _SettingsPageState createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  String? _selectedSex;
  final TextEditingController _ageController = TextEditingController();
  final TextEditingController _weightController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('MediScan'),
      ),
      backgroundColor: const Color.fromARGB(255, 76, 175, 152),
      body: Center(
        child: Container(
          width: 500,
          height: 500,
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.2),
            borderRadius: BorderRadius.circular(10),
          ),
          padding: EdgeInsets.all(20),
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "Please include your information",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 30),
                DropdownButtonFormField<String>(
                  decoration: InputDecoration(
                    labelText: 'Sex',
                    labelStyle: TextStyle(color: Colors.black, fontSize: 20),
                    filled: true,
                    fillColor: Colors.white,
                    enabledBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.black),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.black),
                    ),
                  ),
                  dropdownColor: Colors.white.withOpacity(0.9),
                  style: TextStyle(color: Colors.black, fontSize: 20),
                  value: _selectedSex,
                  items: ['Male', 'Female', 'Other']
                      .map((sex) => DropdownMenuItem(
                            child: Text(sex, style: TextStyle(fontSize: 20)),
                            value: sex,
                          ))
                      .toList(),
                  onChanged: (value) {
                    setState(() {
                      _selectedSex = value;
                    });
                  },
                ),
                SizedBox(height: 20),
                TextField(
                  controller: _ageController,
                  keyboardType: TextInputType.number,
                  style: TextStyle(color: Colors.black, fontSize: 20),
                  decoration: InputDecoration(
                    labelText: 'Age',
                    labelStyle: TextStyle(color: Colors.black, fontSize: 20),
                    filled: true,
                    fillColor: Colors.white,
                    enabledBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.black),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.black),
                    ),
                  ),
                ),
                SizedBox(height: 20),
                TextField(
                  controller: _weightController,
                  keyboardType: TextInputType.number,
                  style: TextStyle(color: Colors.black, fontSize: 20),
                  decoration: InputDecoration(
                    labelText: 'Weight (kg)',
                    labelStyle: TextStyle(color: Colors.black, fontSize: 20),
                    filled: true,
                    fillColor: Colors.white,
                    enabledBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.black),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.black),
                    ),
                  ),
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {
                    if (_selectedSex != null &&
                        _ageController.text.isNotEmpty &&
                        _weightController.text.isNotEmpty) {
                      Navigator.pushReplacement(
                          context,
                          MaterialPageRoute(
                              builder: (context) => Homepage()));
                    } else {
                      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                          content: Text('Please fill in all fields')));
                    }
                  },
                  child: Container(
                    padding: EdgeInsets.symmetric(vertical: 15, horizontal: 30),
                    child: Text(
                      'Save',
                      style: TextStyle(fontSize: 20, color: Colors.black),
                    ),
                  ),
                  style: ElevatedButton.styleFrom(
                    minimumSize: Size(double.infinity, 50),
                    backgroundColor: Colors.white,
                    foregroundColor: Colors.black,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class ResultPage extends StatelessWidget {
  final String sex;
  final String age;
  final String weight;

  ResultPage({required this.sex, required this.age, required this.weight});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('MediScan'),
      ),
      backgroundColor: const Color.fromARGB(255, 76, 175, 152),
      body: Center(
        child: Container(
          width: 350,
          padding: EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.8),
            borderRadius: BorderRadius.circular(10),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text('Result Page', style: TextStyle(fontSize: 24)),
              Text('Sex: $sex', style: TextStyle(fontSize: 20)),
              Text('Age: $age', style: TextStyle(fontSize: 20)),
              Text('Weight: $weight', style: TextStyle(fontSize: 20)),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text('Back'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
