from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.config import settings

router = APIRouter()


integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-17",
      "updated_at": "2025-02-17"
    },
    "descriptions": {
      "app_name": "telex-ci-cd",
      "app_description": "A simple ci/cd slack notifier application",
      "app_logo": "http://ec2-107-23-33-56.compute-1.amazonaws.com/",
      "app_url": "http://ec2-107-23-33-56.compute-1.amazonaws.com/",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier",
    "key_features": [
      "real time update slack notification"
    ],
    "author": "Tayo Jubril",
    "settings": [
      {
        "label": "Time Interval",
        "type": "dropdown",
        "required": True,
        "default": "immediate",
        "options": [
          "immediate",
          "Every 5-min",
          "Every 10-min",
          "Every 1-hour"
        ]
      },
      {
        "label": "slack channel",
        "type": "text",
        "required": True,
        "default": "#DevopsAlert"
      },
      {
        "label": "event type",
        "type": "dropdown",
        "required": True,
        "default": "ci_pipeline",
        "options": [
          "ci_pipeline",
          "cd_pipeline",
          "deployment",
          "error"
        ]
      },
      {
        "label": "message",
        "type": "text",
        "required": True,
        "default": "Basic"
      },
      {
        "label": "include logs",
        "type": "checkbox",
        "required": True,
        "default": "True"
      }
    ],
    "target_url": settings.SLACK_WEBHOOK_URL,
    "tick_url": settings.TICK_URL
  }
}


@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)