import 'package:flutter/material.dart';
import 'screens/home.dart';
import 'screens/prediction_input.dart'; // Import the screen

void main() {
  runApp(GovernancePredictorApp());
}

class GovernancePredictorApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Governance Predictor',
      theme: ThemeData(
        primarySwatch: Colors.teal,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      // Define the named routes here
      initialRoute: '/',
      routes: {
        '/': (context) => const HomeScreen(),
        // '/predict': (context) => PredictionInputPage(), // Named route
      },
    );
  }
}
