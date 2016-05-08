
# channel_routing = {
#     "http.request": "drive.consumers.http_consumer"
# }

from drive.consumers import ws_receive, ws_connect, ws_disconnect

channel_routing = {
    "websocket.connect": ws_connect,
    "websocket.receive": ws_receive,
    "websocket.disconnect": ws_disconnect,
}