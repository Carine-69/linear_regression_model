import 'package:flutter/material.dart';

class PredictionResultPage extends StatelessWidget {
  final String result;

  PredictionResultPage({required this.result});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Prediction Result")),
      body: Center(
        child: Text(
          "Predicted Governance Duration: $result",
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
