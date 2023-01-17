# Dadabot-web

## To start:
### Backend:

    uvicorn api:app --port 8001

### Frontend:

    npm run dev -- --port 8000

### Reverse proxy:

    sudo nginx -c "PATH/TO/FOLDER/nginx.conf"


## Notes:
Converting png to webp and resizing:

    mogrify -format webp -resize 250x150\! chapter*.jpg