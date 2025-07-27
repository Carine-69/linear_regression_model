## Governance Predictor App

This project predicts the strength and duration of a government in African countries using a citizen’s trust in government survey data.
It features a **public FastAPI backend** that serves predictions and a **Flutter mobile app** for easy interaction. The solution addresses governance insight challenges in Africa using machine learning.

---

### 🔗 Public API Endpoint (FastAPI)

**➡️ *https://linear-regression-model-w953.onrender.com/docs*
Use this Swagger UI to test the `/predict` endpoint with JSON input.

Example payload:

```json
{
  "Q20": 3,
  "Q21A": 2,
  "Q24": 1,
  "Q34A": 2,
  "Q26": 1,
  "Q28": 3,
  "Q32A": 4,
  "Q32B": 2,
  "Q48A": 3,
  "Q48B": 2,
  "Q50A": 1
etc
}
```


### 📹 Demo Video (YouTube)

**▶️(https://youtu.be/OCivXTgumCE)), a link to the demo

###  How to Run the Mobile App

1. **Clone the repo**

   ```bash
   git clone https://github.com/Carine-69/linear_regression_model.git
   cd governance-predictor
   ```

2. **Install dependencies**

   ```bash
   flutter pub get
   ```

3. **Run the app**

   * On Chrome (Web):

     ```bash
     flutter run -d chrome
     ```

> Make sure you have [Flutter SDK](https://docs.flutter.dev/get-started/install) installed and a working emulator or device connected.

