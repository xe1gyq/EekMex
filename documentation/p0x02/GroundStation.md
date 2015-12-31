Ground Station
==

## Freeboard.Io

### Setup

1. Go to [freeboard.io](https://freeboard.io/) and sign up
2. Go to [freeboard.io account](https://freeboard.io/account/), under "My Freeboards"
   - "__Enter a Name__" and "__Create New__", let's call it EekMex
   - You should see "__EekMex__" board created being a "__Public__" dashboard
3. Edit EekMex by clicking on "__Edit__" if you want to:
   -  Change the Name
   -  Move to a Private dashboard
   -  Delete
4. Click on [__EekMex__](https://freeboard.io/board/huO_H7) to open the dashboard

### Freeboard EekMex Dashboard

We need to work with

- __Data Sources__ named as "__DATASOURCES__" and initialized by clicking on "__ADD__". They gather data from a specific source as dweet.io, pubnub, or other.
- __Panes__ initialized by clicking on "__ADD PANE__". They hold Widgets
- __Widgets__ display data in some textual or graphical form

The followin Components will be created:

1. Mission Information
   - City
   - State
   - Date
2. Messages
   - Mission Control Center
   - Twitter @EekMex #EekMex
3. Sensors
   - Temperature
   - Pressure
   - Sea Level Pressure
   - Altitude
 4. Position
   - Global Positioning System
 5. Attitude
   - Inertial Measurement Unit

1. Go to "__DATASOURCE__"
   - Type: Dweet.io
   - Name: EekMex Aerospace Learning Platform
   - Thing Name: EekMexArejXe

## Dweet.Io

```sh
    # pip install RandomWords
```

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

### Setup

1. Go to [dweet.io](http://dweet.io/)

    pip install dweepy

## PubNub

### Setup

1. Go to [PubNub](https://www.pubnub.com/) and signup
2. Once logged in, change "App Name" to Eekmex


    # pip install pubnub
