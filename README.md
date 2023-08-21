# Distributed Computing with RQ and Streamlit

This project demonstrates the concept of distributed computing using the Redis Queue (RQ) library for job queuing and execution, along with a Streamlit web application for monitoring and interacting with the distributed tasks. The application fetches content from URLs, counts the number of words in the content, and displays job status, completion times, and metadata through a user-friendly web interface.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Technologies Used](#technologies-used)
- [Acknowledgments](#acknowledgments)

## Overview

Distributed computing involves dividing a complex task into smaller subtasks and processing them concurrently on multiple computing resources, which can result in significant performance improvements. In this project, we use the Redis Queue (RQ) library for task queuing and execution. The Streamlit web application provides a user interface for starting and monitoring jobs, displaying job status, completion times, and associated metadata.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/adgsenpai/distributed-computing-with-rq.git
   cd distributed-computing-with-rq
   ```

2. **Install the required dependencies:**

   Make sure you have Python 3.6 or later installed. Then, install the required packages using pip:

   ```bash
   pip install redis rq streamlit pandas requests
   ```

3. **Run the RQ worker:**

   Start the RQ worker to process enqueued jobs:

   ```bash
   rq worker
   ```

## Usage

1. **Start the Streamlit app:**

   Run the Streamlit app to interact with the distributed computing system:

   ```bash
   streamlit run app.py
   ```

2. **Monitor Jobs:**

   - The app displays the "Refresh Jobs" button. Clicking it retrieves information about completed jobs, including job IDs, completion times, results, and metadata.
   - The "Start Job" button allows you to initiate a new distributed job. Upon clicking it, a job to count words from a specific URL is enqueued, and its progress and status are displayed.

## Components

- **Redis Queue (RQ):**

  RQ is used for queuing and distributing tasks across multiple workers. It allows you to enqueue jobs and process them concurrently, making it a powerful tool for managing distributed tasks.

- **Streamlit:**

  Streamlit is a Python library for creating web applications with minimal effort. In this project, it provides the user interface for interacting with the RQ-based distributed computing system.

- **Python Libraries:**

  The project relies on various Python libraries, including `redis` for connecting to the Redis server, `requests` for making HTTP requests, `rq` for managing the job queue, and `pandas` for data manipulation.

## Technologies Used

- [Redis](https://redis.io/)
- [RQ (Redis Queue)](https://python-rq.org/)
- [Streamlit](https://streamlit.io/)
- [Python](https://www.python.org/)

## Acknowledgments

This project is based on the concepts of distributed computing, job queuing, and web application development. It demonstrates how to harness the power of distributed systems to efficiently complete tasks and provides insights into handling distributed jobs using RQ and Streamlit.

Special thanks to the developers of Redis, RQ, Streamlit, and other open-source technologies used in this project.

---