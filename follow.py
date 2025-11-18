import requests
import json

url = 'https://gql.twitch.tv/gql'

headers = {
  "authority": "gql.twitch.tv",
  "method": "POST",
  "path": "/gql",
  "scheme": "https",
  "accept": "*/*",
  "accept-encoding": "gzip, deflate, br, zstd",
  "accept-language": "en-US",
  "authorization": "OAuth token",
  "client-id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
  "client-integrity": "integrity",
  "client-session-id": "session",
  "client-version": "version",
  "content-type": "text/plain;charset=UTF-8",
  "origin": "https://www.twitch.tv",
  "referer": "https://www.twitch.tv/",
  "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-site",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
  "x-device-id": "ESt0GqJITUWuDVq5Nhds5kwhkWxU73WX"
}

payload = [
  {
    "operationName": "FollowButton_FollowUser",
    "variables": {
      "input": {
        "disableNotifications": False,
        "targetID": "1379063082"
      }
    },
    "extensions": {
      "persistedQuery": {
        "version": 1,
        "sha256Hash": "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"
      }
    }
  },
  {
    "operationName": "FollowButton_FollowEvent_User",
    "variables": {
      "id": "1379063082"
    },
    "extensions": {
      "persistedQuery": {
        "version": 1,
        "sha256Hash": "a3b1fd99e5eac4f46952e3bec90bf41e46adabb7fe865a6aff882983cacfafd2"
      }
    }
  }
]

response = requests.post(url, headers=headers, json=payload)
print(response.json())
