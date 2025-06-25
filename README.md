# 🦊 Zootopia Animal Info Generator

A Python project that fetches animal data via API and generates an attractive HTML page displaying the information.

## 📦 Files

- **`animals_web_generator.py`**
  The main script. It asks the user for an animal name, retrieves data from the [API Ninjas Animals API](https://api-ninjas.com/api/animals), and generates an `animals.html` file with key animal facts.

- **`data_fetcher.py`**
  Handles communication with the API, including data retrieval and basic error handling.

- **`animals_template.html`**
  An HTML template containing a placeholder `__REPLACE_ANIMALS_INFO__` that will be replaced with the generated animal content.

- **`.env`**
  Stores your secret API key. Example content:

  ```
  API_KEY=your_api_key
  ```

## ▶️ Usage

1. **Get an API Key**
   Sign up at [api-ninjas.com](https://api-ninjas.com/) and request an API key.

2. **Set up the project**

   - Install dependencies (only `python-dotenv` and `requests` are needed):

     ```bash
     pip install python-dotenv requests
     ```

   - Create a `.env` file and paste in your API key:

     ```
     API_KEY=your_api_key
     ```

3. **Run the project**

   ```bash
   python animals_web_generator.py
   ```

   Enter an animal like `fox`, and it will automatically generate an `animals.html` file you can open in your browser.

## 🔍 Optional Features

- The `choose_animal_skin_type()` function allows filtering animals by skin type.
- Use `load_data()` to work with local JSON files (useful for offline mode or testing).

## 🛡 Security Tip

Be sure to add your `.env` file to `.gitignore` to avoid exposing your API key in version control:

```bash
.env
```