import json
from datetime import date
import logging

logger = logging.getLogger(__name__)

def load_data():

    file_path = f"./data/YT_data_{date.today()}.json"

    try:
        logger.info(f"Processing file: YT_data_{date.today()}")

        with open(file_path, 'r', encoding='utf-8') as raw_data:
            data = json.load(raw_data)

        # 🔽 KEY NORMALIZATION (minimal + explicit)
        for r in data:
            r["video_id"] = r.pop("Video_id")
            r["video_title"] = r.pop("title")
            r["upload_date"] = r.pop("publishedAt")
            r["duration"] = r.pop("duration")
            r["video_views"] = r.pop("viewCount")
            r["likes_count"] = r.pop("likeCount")
            r["comments_count"] = r.pop("commentCount")

        return data

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise

    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        raise


"""
import json
from datetime import date
import logging

logger = logging.getLogger(__name__)

def load_data():

    file_path = f"./data/YT_data_{date.today()}.json"

    try:
        logger.info(f"Processing file: YT_data{date.today()}")

        with open(file_path, 'r', encoding='utf-8') as raw_data:
            data = json.load(raw_data)

        return data
    
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        raise
"""