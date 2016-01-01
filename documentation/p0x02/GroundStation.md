Ground Station
==


> A ground segment consists of all the ground-based elements of a spacecraft system, as opposed to the space segment, consisting of the spacecraft itself. Ground segment elements may be located together or separately, and may be operated by different parties. Wikipedia

- [Ground Segment Wikipedia](https://en.wikipedia.org/wiki/Ground_segment)

## Software Architecture

### Freeboard.Io

> Freeboard is a turn-key HTML-based "engine" for dashboards. Besides a nice looking layout engine, it provides a plugin architecture for creating datasources (which fetch data) and widgets (which display data)— freeboard then does all the work to connect the two together. Freeboard Github Repository

- [freeboard.io homepage](https://freeboard.io/)

#### Setup

1. Go to [freeboard.io](https://freeboard.io/) and sign up
2. Go to [freeboard.io account](https://freeboard.io/account/), under "My Freeboards"
   - "__Enter a Name__" and "__Create New__", let's call it EekMex
   - You should see "__EekMex__" board created being a "__Public__" dashboard
3. Edit EekMex by clicking on "__Edit__" if you want to:
   -  Change the Name
   -  Move to a Private dashboard
   -  Delete
4. Click on [__EekMex__](https://freeboard.io/board/huO_H7) to open the dashboard

#### Freeboard.IO Components

These are some freeboard.io concepts:

- __Data Sources__ named as "__DATASOURCES__" and initialized by clicking on "__ADD__". They gather data from a specific source as dweet.io, pubnub, or other.
- __Panes__ initialized by clicking on "__ADD PANE__". They hold Widgets
- __Widgets__ display data in some textual or graphical form

### Freeboard EekMex Dashboard

The following widgets will be created:

1. Mission Information
   - Mode
   - Name
   - Launch Site
   - Date
   - Time
   - Mission Control Center Information
3. Sensors
   - Temperature
   - Pressure
   - Sea Level Pressure
   - Altitude
4. Position (Global Positioning System)
   - Latitude
   - Longitude
   - Altitude
   - Satellites
   - Speed
   - Track
5. Attitude (Inertial Measurement Unit)
   - Roll
   - Pitch
   - Yaw

### Freeboard Data Sources

1. Go to "__DATASOURCE__"
   - Type: Dweet.io
   - Name: EekMex Aerospace Learning Platform
   - Thing Name: EekMexArejXe

## Dweet.Io

> Ridiculously simple data sharing for the Internet of Things.

- [dweet.io homepage](http://dweet.io/)

### Setup

```json
{
  "altitude": 1800
  "pressure": "1400"
  "sealevelpressure": "1400"
  "temperature": 21.5,
}
```
  
```Python
    data = {}
    data['altitude'] = altitude
    data['pressure'] = pressure
    data['sealevelpressure'] = sealevelpressure
    data['temperature'] = temperature
    dweepy.dweet_for('EekMexArejXe', data)
```

## PubNub

### Setup

1. Go to [PubNub](https://www.pubnub.com/) and signup
2. Once logged in, change "App Name" to Eekmex

```sh
    # pip install pubnub
```