# Azure Chatbot App (Enterprise Ready)

This is an enterprise-ready Azure Web App Chatbot built with the Bot Framework SDK for Python.

## 📂 Project Structure

```plaintext
src/
  bot/
    main_bot.py         # Main bot logic
    startup.py          # Adapter, state setup
    helpers.py          # Utility functions
  dialogs/
    welcome_dialog.py   # Handles welcome flow
    faq_dialog.py       # Handles FAQ flow
  config/
    settings.py         # Environment settings
  services/
    external_api_service.py  # External API integration
tests/
deployment/
  docker/
    Dockerfile
    runtime.txt
  templates/
    azuredeploy.json

requirements.txt
azure-pipelines.yml
