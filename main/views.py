from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Artist, Song
from main.serializers import ArtistSerializer, ArtistAlbumSerializer


# Create your views here.
def show(request):
    # artist = Artist.objects.order_by("?").first()
    # print(artist)
    # albums = artist.album_set.all()
    # print(albums)
    # for alb in albums:
    #     print(alb.name, alb.release_year)
    #     songs = alb.songs.all()
    #     print(len(songs), "Songs")
    #     for s in songs:
    #         print("Song -", s.name, s.duration)

    song = Song.objects.order_by("?").first()
    print(song)
    album = song.album
    print(album)
    artists = album.artists.all().values("name")
    print(artists)

    # song.album.artists.all()

    return HttpResponse(artists)


@api_view(["GET", "POST"])
def save_or_fetch_artists(request):
    if request.method == "GET":
        artists = Artist.objects.all()
        serializer = ArtistSerializer(instance=artists, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Added artists", "data": serializer.data})


@api_view(["GET"])
def fetch_one_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist)
        return Response(serializer.data)
    except:
        return Response({"error": "Artist not found"}, status=404)


@api_view(["DELETE"])
def delete_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        artist.delete()
        return Response({"message": "Successfully deleted artist"})
    except:
        return Response({"error": "Artist not found"}, status=404)


@api_view(["PUT", "PATCH"])
def update_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    except:
        return Response({"error": "Invalid data"}, status=404)


@api_view(["GET"])
def albums_for_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistAlbumSerializer(instance=artist)
        return Response(serializer.data)
    except:
        return Response({"error": "Invalid data"}, status=404)

# pip install djangorestframework
# RESTFUL services -- apis GET, POST, PUT, PATCH, DELETE, UPDATE
# SOAP services
