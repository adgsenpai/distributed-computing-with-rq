import requests
import rq


def count_words_at_url(url):
    resp = requests.get(url)
    # Access the current job and update its metadata
    current_job = rq.get_current_job()
    current_job.meta['status'] = 'Processing'
    current_job.meta['progress'] = 50  # Update progress to 50
    current_job.meta['Job Name'] = 'Count Words'
    # status
    current_job.save_meta()  # Save the updated metadata

    current_job.meta['status'] = 'Completed'
    current_job.meta['progress'] = 100  # Update progress to 100
    current_job.save_meta()  # Save the updated metadata

    return len(resp.text.split())
