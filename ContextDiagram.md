# SURIMI Context Diagram

The SURIMI System consists currently of 5 models. 
- They run on the Edito Datalab as docker containers.
- Ecopath runs as a replica set of 5 containers, each running 1 simulation
 

```mermaid


flowchart TD
    GUI1["GUI"] --- Controller1["Controller"]
    Controller1["Controller"] --- A@{ shape: processes, label: "Ecopath" }
    Controller1["Controller"] --- Task2["POSEIDON"]
    Controller1["Controller"] --- Task3["Market"]
    Controller1["Controller"] --- Task4["ValueChain"]
    Controller1["Controller"] --- Task5["CMSY++"]


```
- Communication between the containers is done with GRPC. A high performance HTTP/2 web API protocol
- The Controller will run through the timesteps of each simulation
  - It will pass all data between all models (biomass, catches, sales etc.)
  - The way this is done is described in the [Sequence diagram](sequenceDiagram.md)
- Currently the simulation is started with a simple development GUI. This will later be replaced by the MSE GUI and others
- Input (configuration) data and output data is stored in S3 buckets on the Edito Datalab
- An observability system will be in place to log everything that happens on all docker containers
- Every user on the Edito Datalab can run their own version of the SURIMI system for development purposes
- There is also a SURIMI project space that can hold the 'production' SURIMI system 
