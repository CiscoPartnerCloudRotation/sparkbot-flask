# sparkbot-flask

*What it does*
This project is one of three components making up the Cisco Shipped/Sparkbot demo. This component listens for POST requests containing a message on the /post_result endpoint and posts the message received to a spark room. This project requires the sparkbot-google and sparkbot-watcher components to function, and is designed to be containerized and run on the Cisco Shipped platform

*How to Use (With Cisco Shipped)*
1. Fork the repository, as well as sparkbot-google and sparkbot-watcher
2. Configure your Cisco Shipped project to point at the new repository.
3. In your service configuration, set up the AUTH\_KEY environment variable as your Cisco Spark authorization key. Note that AUTH\_KEY identifies a specific user - if you want to post as someone else, or a bot, use their auth key instead.
4. In your service configuration, set up the ROOM_ID environment variable as the Cisco Spark room ID you want to post to.
5. In your service configuration, set up the API_KEY environment variable as your Google Maps API key.
6. In your service configuration, change the Python image to 2.7
5. Build and deploy your service on shipped.