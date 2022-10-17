from website import create_app

app = create_app()


# docker run -p 8099:8099 <image>
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8099, debug=True)