# app.py
from rq import Queue
from redis import Redis
import compute
import streamlit as st
import pandas as pd


st.title('RQ Dashboard')
q = Queue(connection=Redis())
st.write(f"Connected to Redis: {Redis().ping()}")

jobs = []

if st.button('Refresh Jobs'):
    jobs = q.finished_job_registry.get_job_ids()

    # also add time job started
    jobs = [{'id': job_id, 'time': q.fetch_job(
        job_id).ended_at} for job_id in jobs]
    # show result of job
    jobs = [{'id': job['id'], 'time': job['time'],
             'result': q.fetch_job(job['id']).result} for job in jobs]
    # show all meta keys
    jobs = [{'id': job['id'], 'time': job['time'], 'result': job['result'],
             'meta': q.fetch_job(job['id']).meta} for job in jobs]

    st.write(jobs)

# Start job
st.write('Start Job')
if st.button('Start Job'):
    metadata = {'progress': 0}  # Define your desired metadata here
    new_job = q.enqueue(compute.count_words_at_url,
                        'https://adgstudios.co.za', meta=metadata)
    st.write('Job Started!')
    st.write(f'Job ID: {new_job.id}')
