### :scissors: snippet dog :dog2:

#### Intro

I like to write static websites, but I wanted to include some attractive code snippets on my page. 

Rather than rudely off-loading the work to my visitor’s browser with Javascript, I built [**Snippet Dog**](https://snippet.dog) to generate beautiful syntax-highlighted code snippets that are nothing but plain HTML and CSS.

**[Try it out.](https://snippet.dog)**

#### Features

Snippet Dog lets you:

- :globe_with_meridians: highlight the syntax of *tons* of programming languages
- :art: choose from a bunch of different themes
- :1234: enable/disable two different styles of line-numbers

Snippet Dog does *not* let you: customize borders, add drop-shadow, change *[your favorite CSS property here]*. There are too many CSS properties to allow customizing all of them. Instead, Snippet Dog focuses on [doing one thing well](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well): making syntax-highlighted code snippets that you can use on a static website.

#### Technologies

Snippet Dog stands on the shoulders of giants by leveraging some great pre-existing software:

- [FastAPI](https://fastapi.tiangolo.com/) for the Python backend service
  - FastAPI in turn uses [Starlette](https://www.starlette.io/) and [pydantic](https://pydantic-docs.helpmanual.io/)
- [Pygments](https://pygments.org/) for the syntax highlighting
- [jQuery](https://jquery.com/) for Ajax and client-side interactivity

In production, Snippet Dog relies on:

- [Gunicorn](https://gunicorn.org/) for WSGI server
- [Uvicorn](https://www.uvicorn.org/) for ASGI server
- [Docker](https://www.docker.com/) for containerization
- [nginx](http://nginx.org/) for reverse proxy
- [DigitalOcean Droplet](https://www.digitalocean.com/products/droplets/) for VM

#### Resources

I’m not an expert on server configuration. Here are some tutorials I used to get my server set up.

1. Create a DigitalOcean Droplet using the [Ubuntu with Docker image](https://marketplace.digitalocean.com/apps/docker
   )
2. [Initial Server Setup with Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04
   )
3. [How To Install Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)
4. [How To Redirect www to Non-www with Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-redirect-www-to-non-www-with-nginx-on-ubuntu-14-04) (works just fine on Ubuntu 18.04)
5. [How To Secure Nginx with Let's Encrypt on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)

And here are some docs I consulted while troubleshooting some nginx configuration stuff:

- [Stack Overflow - How to Configure NGINX to Serve ASGI from UNIX Socket?](https://stackoverflow.com/questions/57532987/how-to-configure-nginx-to-serve-asgi-from-unix-socket)
- [Deploying Gunicorn - Nginx Configuration](https://docs.gunicorn.org/en/stable/deploy.html)
- [Uvicorn - Deployment - Running behind Nginx](https://www.uvicorn.org/deployment/#running-behind-nginx)