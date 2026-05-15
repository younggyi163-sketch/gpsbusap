[app]

title = GPS Bus App

package.name = gpsbus

package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,kv,json,mp3

version = 1.0

requirements = python3,kivy,plyer,geopy,requests,pyjnius,kivy_garden.mapview

orientation = portrait

fullscreen = 0

android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,INTERNET
