// import the material.dart from the flutter package. This holds the default styles.
import 'package:flutter/material.dart';

// This is the main entry point of the app. When it is launched this is what runs.
void main() {
  runApp(const MyApp());
}

// Widget is just a class. So we are extending the capability of a StatelessWidget.
class MyApp extends StatelessWidget {
  // constructor
  const MyApp({super.key});

  // override the base functionality
  @override
  Widget build(BuildContext context) {
    // Material App root widget
    return const MaterialApp(
      title: 'Todo App',
      home: Scaffold(),
    );
  }
}
