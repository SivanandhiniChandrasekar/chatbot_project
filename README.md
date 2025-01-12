# CDP Support Agent Chatbot

## Project Overview
This project is a chatbot that helps users find answers to "how-to" questions related to four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot extracts relevant information from the official documentation of these platforms and provides the user with step-by-step guidance.

## Features
- **Answer "How-to" Questions**: The chatbot can respond to user queries about how to perform tasks in Segment, mParticle, Lytics, and Zeotap.
- **Extract Information from Documentation**: The chatbot can navigate through the official documentation of each platform and extract relevant instructions.
- **Handle Variations in Questions**: The chatbot handles variations in phrasing and terminology.
- **Bonus Features**:
  - **Cross-CDP Comparison**: The chatbot can compare functionalities between the platforms.
  - **Advanced "How-to" Questions**: The chatbot can answer more complex questions related to integrations and configurations.

## Data Sources
The following official documentation is used to retrieve information:
- **Segment Documentation**: [Segment Docs](https://segment.com/docs/?ref=nav)
- **mParticle Documentation**: [mParticle Docs](https://docs.mparticle.com/)
- **Lytics Documentation**: [Lytics Docs](https://docs.lytics.com/)
- **Zeotap Documentation**: [Zeotap Docs](https://docs.zeotap.com/home/en-us/)

## Technologies Used
- **Python**: Backend programming language.
- **Flask**: Web framework to create the chatbot interface.
- **NLTK**: Natural Language Processing for query analysis.
- **HTML/CSS/JavaScript**: Frontend for creating the chatbot user interface.

## Installation Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/kaif-g/chatbot_project.git
   cd chatbot_project
2. Install the required dependencies:
   pip install -r requirements.txt
3. Run the Flask app:
   python app.py
   
