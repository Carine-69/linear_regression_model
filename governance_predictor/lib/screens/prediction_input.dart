import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'prediction_results.dart';

class PredictionInputPage extends StatefulWidget {
  @override
  _PredictionInputPageState createState() => _PredictionInputPageState();
}

class _PredictionInputPageState extends State<PredictionInputPage> {
  final _formKey = GlobalKey<FormState>();
  final Map<String, TextEditingController> controllers = {};

  final List<Map<String, String>> fieldDetails = [
    {"key": "Q20", "label": "Experience of corruption? (1.0–8.0)"},
    {"key": "Q21A", "label": "Trust in courts of law? (1.0–8.0)"},
    {"key": "Q24", "label": "Preference for democracy? (1.0–8.0)"},
    {"key": "Q34A", "label": "Gov’t handling of education? (1.0–8.0)"},
    {"key": "Q26", "label": "Freedom to express views? (1.0–8.0)"},
    {"key": "Q28", "label": "Media freedom from government? (1.0–8.0)"},
    {"key": "Q32A", "label": "Fairness toward your ethnic group? (1.0–8.0)"},
    {"key": "Q32B", "label": "Fairness toward other ethnic groups? (1.0–8.0)"},
    {"key": "Q48A", "label": "Gov’t help during COVID? (1.0–8.0)"},
    {"key": "Q48B", "label": "NGO help during COVID? (1.0–8.0)"},
    {"key": "Q50A", "label": "Importance of top issue? (1.0–8.0)"},
    {"key": "Q50B", "label": "Importance of second issue? (1.0–8.0)"},
    {"key": "Q50C", "label": "Importance of third issue? (1.0–8.0)"},
    {"key": "Q51A", "label": "Ease of getting IDs? (1.0–8.0)"},
    {"key": "Q51B", "label": "Ease of school enrollment? (1.0–8.0)"},
    {"key": "Q53A", "label": "Access to clean water? (1.0–8.0)"},
    {"key": "Q53B", "label": "Access to toilet facilities? (1.0–8.0)"},
    {"key": "Q53C", "label": "Access to medical services? (1.0–8.0)"},
    {"key": "Q35A", "label": "Gov’t handling of economy? (1.0–8.0)"},
    {"key": "Q36A", "label": "Gov’t addressing unemployment? (1.0–8.0)"},
    {"key": "Q38A", "label": "Gov’t addressing poverty? (1.0–8.0)"},
    {"key": "Q38B", "label": "Gov’t handling income inequality? (1.0–8.0)"},
    {"key": "Q38C", "label": "Gov’t handling taxation fairness? (1.0–8.0)"},
  ];

  @override
  void initState() {
    super.initState();
    for (var field in fieldDetails) {
      controllers[field["key"]!] = TextEditingController();
    }
  }

  @override
  void dispose() {
    for (var controller in controllers.values) {
      controller.dispose();
    }
    super.dispose();
  }

  Widget buildTextField(String key, String label) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: TextFormField(
        controller: controllers[key],
        decoration: InputDecoration(
          labelText: label,
          border: OutlineInputBorder(),
        ),
        keyboardType: TextInputType.numberWithOptions(decimal: true),
        validator: (value) {
          final val = double.tryParse(value ?? '');
          if (val == null) return 'Enter a valid number';
          if (val < 1.0 || val > 8.0)
            return 'Value must be between 1.0 and 8.0';
          return null;
        },
      ),
    );
  }

  void predict() async {
    if (!_formKey.currentState!.validate()) return;

    final inputData = {
      for (var field in fieldDetails)
        field["key"]!: double.parse(controllers[field["key"]!]!.text),
    };

    final uri = Uri.parse(
      "https://linear-regression-model-w953.onrender.com/predict",
    );

    try {
      final response = await http.post(
        uri,
        headers: {"Content-Type": "application/json"},
        body: jsonEncode(inputData),
      );

      final json = jsonDecode(response.body);
      final prediction =
          json["Governement duration prediction"] ??
          json["prediction"] ??
          "No prediction returned";

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (_) => PredictionResultPage(result: prediction.toString()),
        ),
      );
    } catch (e) {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(SnackBar(content: Text("Prediction failed: $e")));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Governance Prediction")),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: SingleChildScrollView(
            child: Column(
              children: [
                const Text(
                  "Fill out each question below. Your answers will be sent securely to the model for a prediction.",
                  style: TextStyle(fontSize: 16),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 16),
                ...fieldDetails.map(
                  (field) => buildTextField(field["key"]!, field["label"]!),
                ),
                const SizedBox(height: 20),
                ElevatedButton.icon(
                  icon: Icon(Icons.analytics),
                  label: Text("Predict"),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.teal,
                    padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                  ),
                  onPressed: predict,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
