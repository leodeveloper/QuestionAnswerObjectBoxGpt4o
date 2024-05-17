# QuestionAnswerObjectBoxGpt4o
Question Answer application using  ObjectBox vector database, Gpt4o and langchain

![Chat Bot Image](https://github.com/leodeveloper/QuestionAnswerObjectBoxGpt4o/blob/main/llama3%20objectbox%20vectordb.png)

# RAG QuestionAnswer Application with ObjectBox, GPT-4, groq, llama3, and LangChain

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

This project is a Retrieval-Augmented Generation (RAG) QuestionAnswer application that extracts information from any website and answers questions based on the extracted data. The application leverages the ObjectBox vector database for efficient data storage and retrieval, GPT-4 for natural language understanding and generation, and LangChain for seamless integration of these components.

## Features

- **Data Extraction:** Extract content from any website.
- **Vector Database:** Use ObjectBox for efficient storage and retrieval of data in vector format.
- **Advanced Q&A:** Utilize GPT-4 for answering questions based on extracted data.
- **LangChain Integration:** Streamlined process for managing data flow and interactions between components.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/leodeveloper/QuestionAnswerObjectBoxGpt4o
    cd QuestionAnswerObjectBoxGpt4o
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up ObjectBox:**

    Follow the instructions to install and set up ObjectBox from [ObjectBox's official documentation](https://objectbox.io/documentation/).


## Configuration

Configuration settings for the application are managed in the `config.yaml` file. Key settings include:

- **ObjectBox database path**
- **API keys and tokens for GPT-4**
- **Extraction parameters**

Make sure to update this file with your specific settings before running the application.

## Contributing

We welcome contributions to improve this project! Here’s how you can help:

1. **Fork the repository.**
2. **Create a new branch:**

    ```sh
    git checkout -b feature-name
    ```

3. **Make your changes and commit them:**

    ```sh
    git commit -m "Description of changes"
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature-name
    ```

5. **Submit a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **OpenAI:** For GPT-4
- **ObjectBox:** For the vector database solution
- **LangChain:** For the powerful integration framework

We appreciate all the tools and libraries that have made this project possible.

---

Feel free to reach out at leodeveloper@gmail.com if you have any questions or need further assistance. Happy coding!
