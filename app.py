##Imports
    import datetime as dt
    import numpy as np
    import pandas as pd
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    from flask import Flask, jsonify

##Engines & Database
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    
    # Save references to the measurement and stations tables
    Measurement = Base.classes.measurement
    Stations = Base.classes.station
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Flask Setup
    app = Flask(__name__)
    
    # Flask Routes
    @app.route("/")
    def welcome():
        """List all available api routes."""
        return (
            f"Avalable Routes:<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/<start><br/>"
            f"/api/v1.0/<start>/<end>"
            )
    
## /api/v1.0/precipitation
    @app.route("/api/v1.0/precipitation")
    def precipitation():
        last_yr = dt.date(2017,8,23) - dt.timedelta(days = 365)
        last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
        precipitation = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date > last_yr).order_by(Measurement.date).all()

    
    # Convert the query results to a Dictionary using date as the key and prcp as the value
        precipitations = []
        for result in results:
            row = {}
            row["date"] = result[0]
            row["prcp"] = float(result[1])
            precipitations.append(row)
    
        return jsonify(precipitations)
    
    
    ## /api/v1.0/stations
    @app.route("/api/v1.0/stations")
    def stations()
        results = session.query(Stations.name).all()
        all_stations = list(np.ravel(results))
        return jsonify(all_stations)
    
    ## /api/v1.0/tobs
    @app.route("/api/v1.0/tobs")
    def temperature():
        results = session.query(Measurement.tobs, Measurement.date)
        filter(Measurement.date > '2016-08-23')
        order_by(Measurement.date).all()

    # Convert the query results to a Dictionary using date as the key and prcp as the value.
        temperatures = []
        for result in results:
            row = {}
            row["date"] = result[0]
            row["tobs"] = float(result[1])
            temperatures.append(row)
        return jsonify(temperatures)

## /api/v1.0/<start> and /api/v1.0/<start>/<end>
    
@app.route("/api/v1.0/<start>")
def calc_temps_start(start):
     start = datetime.strptime('2016-08-23', '%Y-%m-%d').date()
     start_results = session.query(func.avg(Measurement.tobs),func.max(Measurement.tobs),func.min(Measurement.tobs).\
               filter(Measurement.date >= start)
     start_tobs_list = []   
     for i in start_results:
       dict = {}
       dict["TMIN"] = float(tobs[1])                     
       dict["TMAX"] = float(tobs[0])
       dict["TAVG"] = float(tobs[2])
       start_tobs_list.append(dict)
     return jsonify(start_tobs_list)                    
                            
@app.route("/api/v1.0/<start>/<end>")
def calc_temps_end(start,end):
     start = datetime.strptime('2016-08-23', '%Y-%m-%d').date()                      
     end = datetime.strptime('2017-08-23', '%Y-%m-%d').date()
     end_results = session.query(func.avg(Measurement.tobs),func.max(Measurement.tobs),func.min(Measurement.tobs).\
               filter(Measurement.date >= start)                     
     start_end_tobs_list = []
     for i in start_end_tobs_list:
       dict = {}
       dict["TMIN"] = float(tobs[1])                     
       dict["TMAX"] = float(tobs[0])
       dict["TAVG"] = float(tobs[2])
       start_end_tobs_list.append(dict)
     return jsonify(start__end_tobs_list)   

    if __name__ == "__main__":
        app.run(debug=True)
