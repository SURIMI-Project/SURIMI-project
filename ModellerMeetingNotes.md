# [SURIMI] WP3 Modellers Meeting -- 2026-10-06

## Action points

### Status Deliverables
| ID | Model | Owner | Status Model | Status Report | Status Review |
|---|---|---|---|---|---|
| D3.1 | System dynamics model | NORCE | ready | ready | send to Jeroen |
| D3.2 | Product flow value-chain model | EII | not ready| not ready| |
| D3.3 | Agent-based model | OXF | ready | ready | review Timo and Jeroen|
| D3.4 | MICE ecosystem model | AUTH | | | |
| D3.5 | EwE model | EII | | | |
| D3.6 | CMSY++ assessment model | AUTH | | | |
| D3.7 | NLP assessment model | NORCE | ready | ready | Oender reviewed, review Timo this week |
| D3.8 | MSE policy model | OXF/EII | | | review Nic, add a sentence why it's not R |
| D3.9 | NLP policy model | NORCE | ready | ready | Oender reviewed, review Timo week|


### STORAGE Problem
- Edito currently provides us 50 GB storage, one NetCDF is about 400 MB. 
- Ideas: Limit the output to specific user requests? 
- Discussion  in Copenhagen


### AWGEAN case
- MICE uses functional groups instead of species (how to communicate in grpc?)


# [SURIMI] WP3 Modellers Meeting -- 2026-10-06

## Action points

- LICENSES DISCUSSION:

  - Our aim is to use a permissive license such as Apache 2.0 which commits the code to be open and available while at the same time allowing other interested users to extend it for both open and commercial purposes.
  - What license should the input data use?
    --> Question to the commissioner: e.g. What to do with the combined data used in POSEIDON.

- Repository SURIMI Project

  - We could have organization level websites hosted on GitHub (for models and project wiki)
  - Also create an organizational level README.md to create a roadmap for the project.
  - Add to website a link to the repo

## Team updates

### EII

- SURIMI project on EDITO has increased memory now, 2 MSE runs (witth each 5 simulatitons) can run at the same time now.
- New messages about value chain model outputs will be generated.

### NORCE

- North-western Mediterranean finished on Thursday.
- LLM deliverables are almost finished. Review Meeting on Monday.

### AUTH

- Deliverables are updated.

### UOXF

- Working on deliverables and documentation, fixing bugs related to that.


# [SURIMI] WP3 Modellers Meeting -- 2026-09-23

## Action points

### The talk Patrycja and RIK had with the EDITO team.
- Edito will upgrade of the Kubernetes cluster.
	- Can then provide observability as a service (Metrics, Logging and Tracing)
	- Authentication as a service 
	- Better support for gRPC
	- Available resources to run many MSE simulations
- We get more resources (cpu, memory)
- We investigate how we can optimize the use of Kubernetes
- New EDITO Viewer
- There is no more development on the general EDITO Viewers, so we won’t be using them in SURIMI
	- New S3 bucket (move away from Minio)
- I will investigate and report
--> The minutes of this meeting can be found on SharePoint (WP4/EDITO)

### The deliverable template we discussed with Nicolas.
--> List of deliverables: https://github.com/Official-EwE/SURIMI-project/tree/main/deliverables
- Template proposal with:
	- Sequence diagram with only the model interactions
	- Configuration (list of files, necessary to run the model)
	- Input messages
	- Output messages
- Write them in markup. When everything is done, NORCE will convert them to the Word template. (Except CMSY++, which is already a Word document)

- --> Date for Review: Drafts need to be ready be fore the 23.10.
- --> 5-10 pages
- --> Additional information can live in the Github repository
- 


- The mice model is not really a separate model. In the deliverable we will describe that we have created 3 scenarios (northwestern_med, aegean_sea and anchovy_bay) for which we created configuration files. 
- The Aegean sea model configuration files (EwE database etc.)



- Problem: Mice model parametrisation cannot be shared.
	- Attange chat with Patrycja about that! Do we need a discussion with EU officer?
	
- Should we leave the project on the EwE repo or the SURIMI projec
	- we will test it with poseidon and LLM
	- Timo invites all members
	

## Team updates

### EII
- Agean model Team meeting will be arranged by Jeroen, he reaches out to Thanassis. 

### KONNECTA
- ss 

### NORCE
- NET CDF update will be updated by RIK
- 

### AUTH
- 

### UOXF

- 

## To-dos

- [ ] Meeting with Villy for Anchovy Bay ()

---


# [SURIMI] WP3 Modellers Meeting -- 2026-09-09

## Action points

1. Model GUI: discussion on stakeholder workshop feedback
- Aristea needs feedback from all the Modellers
- Aristea is sending around an event 

2. The templates for deliverables
- Auth has an additional script for the functional groups

3. LLM surveys - Hasan
please go aheadplea
- tries to send it to individual persons to increase response rate\
- 

4. Social Simulation Coference 2026

## Team updates

### EII

- MSE calculations are running in EDITO,  
- experiments with up to 5 simulations can run simulataiously
- change in SURIMI protocol --> to add climate scenarios, this can also be used to 
- Rik is joining the EwE course at the end of October, together with Jeroen and Nic

- Patrycja and Rik are trying to arrange some meetings with the DAtalab people, but so far without sufficient results. We can continue without their help.
- HAsan can now book more gpu time, the processes are now not ended after 3 hours. --> Now he can run models for multiple weeks.
- 

### KONNECTA
- 

### NORCE
- 

### AUTH
- 

### UOXF

- 

## To-dos

- [ ] Meeting with Villy for Anchovy Bay ()

---

# [SURIMI] WP3 Modellers Meeting -- 2026-07-15

## Round table

### Aristea

- Sent a Miro board by email. Took Ana's transcript and wrote down all the feedback that we need to address. Added the issue type, the most relevant people, and priorities. There are 35 issues overall, so we'll need to discuss them. Will send out a Doodle for biweekly meetings.
- Copernicus has a new call for tenders out; deadline is 23 August. Looking for proposals on "coastal demonstrators". We could do something around adapting the SURIMI framework to directly use live data from Copernicus. Proposals should not exceed 15 pages, so it should be manageable. Aristea will share the documentation.

### Rikk

- Has been busy making the Controller more reliable. Can now run experiments, cancel them, and restart them in a more robust way. Can configure the number of ports used directly from EDITO, making it easy to run multiple EwE instances.
- NetCDF output files are mostly finished. They can grow quite large (up to 750 MB for simulations up to year 2050 with five parallel MSE runs).

### Jeroen

- Implementing changes to the market model to retrieve prices from national markets.
- Has obtained the Aegean Sea model and is starting work on it.
- Villy is still working on Anchovy Bay, so it may be a while before we can arrange a meeting with him.
- Will meet with Nicolas in the coming days regarding biomass map generation for calibrating POSEIDON.

### Khai

- Has been doing a lot of bug fixing on the market model and setting up unit and integration tests to make this process easier in the future.
- Has been working with Timo on price generation.

### Thanasis

- Gave the EwE Aegean Sea model to Jeroen; running CMSY++ for the Aegean Sea.
- Will send out a draft of the model deliverable before the August holiday. We can use it as a template for discussing what the deliverables for the other models should look like.

### Nicolas

- Worked on setting things up for POSEIDON calibration, tweaking the inputs to the market model and various technical issues around the protocol.
- Met with Miquel to discuss bottom trawler regulations

## Architecture documentation

Rikk wrote a detailed LLM prompt for generating technical documentation for the Controller model and suggested using the same approach for the other SURIMI models.

He will go through all the repositories, try it out, and let us know so we can review whether it produced good documentation.

# [SURIMI] WP3 Modellers Meeting -- 2026-07-01

## To-dos 
- [ ] Create a template for the model deliverables
	- Timo Creates a meeting
- [ ] Meeting with Evelina:
	-  to check if prices are already in data lake / gui
	- discuss source of landings for calibration of CMSY++
	- *Timo contacts*
- [ ] Meeting with Villy for Anchovy Bay
	- **Jeroen, this needs to happen very soon !!!!!!!!!!!**
- [ ] Meting between NORCE and UOXF

## Team updates

### KONNECTA

- recovers from deliverable intense period
- needs to speak to RIK about connection between NETCDF model output.
	-> model gui has deadline in spring
- still waits for the report from workshop
- Leonidas is in direct contact with EDITO team
	- communication through email with Raphael
	- quick responses
	- some problems with gitlab
	- good communication so far

### NORCE 

#### Market

- fixed a plenty of bugs, most importantly..
	- changed the way market model handles parameters for price calculation (now its easy to change them, i.e. add or remove, related to change from gear_code to category_code.
	- market model is now taking "current_date_time" into account, GetSpeciesPrices, UpdateSales, and SimulateStep (GetSpeciesPrices not tested yet)
	- change in the way the handle synchronising the western_med config-files, there is now a script *./scripts/update_config.py*
	- market model is no longer taking negative landings, or landings that are closing in towards 0 (python floating point precision, IEEE 754)
- started working on the calibration of western_med.
- to prepare for Aegean Sea and the changes regarding to the market structure in Western Med, we conceptualised a different structure of the market system to local and national markets.

Questions:
- we need the updated sales message gRPC
	- remove unused markets and add category code to regenerate the files manually
	- two ports have been removed because these ports did not have local markets (related vessels go to neighbouring port)
- discussion on national prices and weights to calculate them (are there any local markets involved that are not in the contract)
	- some other local ports were also included to calculate the weighted mean (most likely very minimal influence)
- species prices and landings for Aegean Sea, are they on data lake ?
	- data most likely not in data lake
	- double check if prices are on EMODNET @ Nicolas will do that

#### LLM
- started curating the benchmark data, checking which one is hallucinated, wrong, or we missed some clearly important questions to benchmark: SURIMI-mcp/benchmark at master 
- https://github.com/Official-EwE/SURIMI-mcp/tree/master/benchmark
- Hasan is coming back at the end of the week, Oender goes on holidays

### AUTH 

- R script to aggregate stock status per functional 
- work on MICE for Aegean sea is progressing 

### UOXF 
- new data created for species prices in western_med, now based on EMODNET data with new location (national and local)
- changes to protocol and following changes to POSEIDON
- continuous calibration efforts
	- Question regarding landings:
		- CMSY++ uses the dataset provided by Evelina, source will be clarified


## Other topics
- consortia call slides
- pushing meeting notes to SURIMI-project repo


## NEXT Meeting
- making sure we are using coherent landing data to calibrate all the models
- make sure that the models also cover that same spatial region (is GSA6 in all models the same)
-->  will there be any tutorials during SEAtwins Symposium, 2026 2.-6. November 2026

---

# [SURIMI] WP3 Modellers Meeting -- 2026-06-17

## To-dos
- [X] File: Realistic update sales messages from Poseidon and EwE to develop integration test for *Market Model*
- [ ] Create a template for the model deliverables
- [x] Meeting: Clarify the the differences between the "NLP policy model" and the "NLP assessment model", and what exactly will be delivered in D3.7 and D3.9
- [x] Meeting: Aegean Sea, start discussion
- [x] Meeting: Prices for species

## Team updates

### EII 
@Jeroen: In deliverable model
--> after he will work on the deliverable

@Rik: 
- getting the experiments and the MSI runs working and writing it in NETCDF files
	- bugs were fixed and now multiple Simulations can run at the same time
- discussion with Patrycja on how to involve EDITO more
	- Rik: has a list of issues to discuss

### NORCE 

#### Market

- prices are no longer static and now differentiate by gear code and category

- integrated with EDITO and connected to S3 buckets for input data
	- the market model should now run as part of the pipeline

- refactored the codebase to improve maintainability:
	- added unit tests , ongoing
	- implemented multithreading, ensuring all sales messages are captured correctly
	
- To-do: make sure scenarios are used for input files on S3

#### LLM

- reworked the model after the last internal meeting 
- is currently testing with different personas to decrease hallucination
- answers by LLM will have option to verify in data, with link to corresponding datasets.
- @all test the use cases for your model!
--> https://project-surimi-vllm-ui.lab.dive.edito.eu/


### UOXF
- calibrated and sanity tested with Ernesto's Indonesian model
- To-do: get data from s3 buckets

### AUTH

@Maria
- script is faster now
- testes functional groups for Aegean and Western Med

@Athanasios
- MICE for Aegean is almost finalised.

## Discussion on potential new data source for species prices
 
- EDMODNET Data
	- EMODNET provides price and landing data by port and species
	- data starts at 2015 to 2025, has monthly information
	- can be queried directly from EMODNET (Web Feature and Coverage Services (WFS/WCS)
	
- category_code vs gear_code
- how to deal with missing data, when in past. (market model)
 
- --> have a meeting **Michael Ortega
- --> https://ows.emodnet-humanactivities.eu/geonetwork/srv/api/records/ff5f738f-94ee-4704-94c2-7c951c931973
- --> have a meeting with Evelina to check about how it overlaps with the data in the DATA gui

---

# [SURIMI] WP3 Modellers Meeting -- 2026-06-03

## Team updates

### EII 

- Refactoring after discussions in Brussels
- continued work on NetCDF output
- all docker images are now hosted on github (ghcr.io/official-ewe)

### KONNECTA

- still waiting for workshop transcript 

### NORCE 

#### LLM

- working on deployment of LLM on EDITO
	- our own model and cloud based 
	- possible to connect MCP for more capabilities e.g. to generate graphics etc.
- next steps is to 
	- test and address hallucination 
	- connection to "real" data on EDITO, Aristea can provide access to S3 bucket
	
- https://project-surimi-vllm-ui.lab.dive.edito.eu/
- next meeting will have a demo

#### Market

- static prices identified
- working on integration test

- questions:
	- @Nicolas: Meeting with Nicolas to discuss the fish price data situation.
		- category_code replaces gear_code. 	
	- @Nic and Jeroen: Need some realistic update sales messages from Poseidon and EwE to develop integration test.
		- Rik will send them to us
	- @Nic Ernestos "old" model
		- it's most likely on the Poseidon repo
	- @Rik: Meeting with Rik on the static price issue
		- discuss Grpc calls, data structure and values of UpdatesSales message 


### AUTH 

- Integration tests with Rik
- add new service to generate stock status for the Interface.


### UOXF
- continues work on calibration for the next weeks.
	- trying to reproduce Indonesia model

- meeting with CNR
		- found operation costs data from EU data collection framework (DCF): national fleet reports
		- https://stecf.ec.europa.eu/data-dissemination/aer_en, already in data lake
		- working on integration into model


## Planning ahead: 

### Use cases 2 and 3
- planning when to test with real data Aegean Sea (MICE and no Poseidon)
	- new prices
	- new contract 
	- change the controller to make Poseidon optional 
- --> meeting to be planned by Athanasios
	
-  for planning Anchovy Bay 
- --> meeting with Villy required (MICE and Poseidon)
	- use of real environment data
	- base prices on Mediterranean model
	- to simplify thing we can stay on functional group level
		- also exemplifies that you can use the model combination on different resolutions 
		
= --> for both cases we need to create a list of files that we need to export from the EwE model, for other models to Use

= --> create a template for the model deliverables 
- for D3.8 we need to work a bit on the framing 

= --> MEETING !!!  Clarify the the differences between the "NLP policy model" and the "NLP assessment model", and what exactly will be delivered in D3.7 and D3.9
	
- deliverable D4.6 – Policy reports supporting strategic marine interventions
	- Mentions MPAs and Subsidies explicitly 
	- needs to be integrated in MSE tool 
	- possibly also needs new messages
	- contributions from the last
	- make sure that the deliverable is not over promising (there is a tension here between policy analysis and actual TRL level we are achieving in the project)
- CHECK that the deliverable will be delayed or changed
	
-  @Timo--> mention at next consortium meeting, and talk to @Patrycja

---

# [SURIMI] WP3 Modellers Meeting -- 2026-05-20

## Team updates

### KONNECTA
- waiting on the transcript of the Workshop
- planing data interface on EDITO

### NORCE
- Khai joins the team on Thursday
- example files will be in GitHub *Surimi protocol repo, messages for postman will be in json

- Hasan: 
	- will transfer the package to SURIMI project GitHub Rikkert will help
	- SURIMI MCP will be on EDITO, will compare MCPs and locally hosted solutions
	- EDITO support might help with storage limitation
	- model gui integration needs to be clarified, especially after the workshop it seems that users are not to interested in interpretation by LLM/

### CNR
- cleaned the data in the data gui

### EII 
- Jeroen:
	- works on Value Chain
	- wants to talk to EDITO on a streamlined process to integrate other model like climate etc. 

- Rik:
	- worked on the Orchestrator integration of aggregation
	- designed a new structure for protobuf messages
	- integration to Market and Poseidon in progress, same will be happening to CMSY in the future

## Topics to discuss
@ Rik
- the refactoring process after the discussions about Simulations, experiments and aggregation
- the involvement of the people of EDITO / Mercator Ocean
- the output of CMSY++ should be decided on. got an output file of CMSY with 323 columns. We should decide on what to display in the Model gui, so we can decide which of the fields should be in the StockAssesment output message

---

# [SURIMI] WP3 Modellers Meeting -- 2026-04-22

## Team updates

### EII 

- Github asked to use data to train Copilot.
	- --> Norces Github copilot enterprise opts out by default.

### KONNECTA

- Model GUI
	- Aristea
		- added a comparative dash board to be able to compare to scenarios
		- will be added to the video 
		- at some point we will improve this for the final product
	- Jeroen
		- overlap Matrix is a nice way to work with overlapping polygons to e.g show trends in time or differences in two scenarios with colours and transparency (Athanasios project)
		- models can produce shape files for the interface to use
	- updated google doc of model descriptions on modelGui
		- @all work on the descriptions of their model https://teams.microsoft.com/l/message/19:meeting_NzViYTU2ZDEtNzc2My00ZTQwLWE3MGItNzZlYTU3YTgzNzU0@thread.v2/1775654176208?context=%7B%22contextType%22%3A%22chat%22%7D

### NORCE 

- PPT Trust session – Building trust in the data, models and outputs
- interface section for model
- SSC panel

- LLM (SURIMI ASSISTANT)
	- tried to connect LLM to the Model interface
	- wants to add this to data hubs and Jupyter notebook
	- discussion on this will follow up in the next weeks
		- Possibilities of using LLM in Data user interface and also in Model gui

### UOXF
- working on calibration for the next weeks.


## Other topics
- tutorial kits
 
 ---
 
# [SURIMI] WP3 Modellers Meeting -- 2026-04-08

## Team updates

### EII 

- Jeroen
	- spatial MSE in Ecopath is developed as a separate model for SURIMI (@conceptualisation phase)
	- semantic wrapper for Ecopath and the Value chain
- Rik
	- S3 Buckets have been changed, resulting in connection errors in .NET services. EDITO is searching for alternative IO storage provider (moving away from MinIO) , https://cloudferro.com/ is the current cloud provider of EDITO 
	- all output of SURIMI models is stored in NetCFT files, the file is constructed at the end of simulation because it is very work intensive. 
		- Panoply
- Villy
	- will work with user interface

### KONNECTA

- Aristea
	- working heavily on the modelGui, especially action points form the last Meeting
		- functional grouping
		- working with Athanasios data sheet
	- updated google doc of model descriptions on modelGui
		- @all work on the descriptions of their model https://teams.microsoft.com/l/message/19:meeting_NzViYTU2ZDEtNzc2My00ZTQwLWE3MGItNzZlYTU3YTgzNzU0@thread.v2/1775654176208?context=%7B%22contextType%22%3A%22chat%22%7D
	- DataGui is almost finished
		- WP2 Partners already used the tool heavily
		- Deliverable is sent out for internal review

### NORCE 

- Timo
	- works on market model 
	- works on abstract for presentation at SSC *24th to 28th of August

- Oender 
	- Hassan was on boarded (experienced in LLM based systems)
	- internal prototype is worked, prototype will be shown in two weeks

## Other topics
- periodic Reporting Feedback D5.2 - Quality Assurance and risks management
	- special attention should be given to MSE development (Jeroen)
	- continuous integration tests will be visible when Rik runs them periodical
	- we need to make sure that our SURIMI graphs and info material are aligned with the capabilities of the model, this also means that we need to double check what we promised in the proposal (@all we need to bring that into the next consortium meeting) (e.g. might want to use heat maps to show the effort of trawlers)

- Anchovy bay map is still under development (might be related to Cambridge Bay)

- training day 4th of Nov - SeaTwins Symposium
	- for educational purposes we could use the Anchovy bay 
	- preference of WP3 is to not to have the training

---

# [SURIMI] WP3 Modellers Meeting -- 2025-12-03

## Digital Ocean Forum - Brussels
- Edito has a map viewer
- Edito also implemented a new viewer
- plan how to bring our data to the data catalogue
	- at the moment data is dumped into root, this will be changed in the next couple of month.
	- for this data set needs to be stackify
- Edito is investing into increased user support and services, also a forum (expected in march)
- maybe there is a possibility to connect to other services provided by EDITO, like Copernicus (climate scenarios) or EMODNET
- data needs to be in S3 container (KONNECTA is already working on this)

## Data & Interface
- two types of data:
	- model data (This data will be on the data lake at the end of the project)
	- scenario Data (data to inform scenarios)
	- model outputs (outputs in model gui, outputs that are only stored in data lake)

## Protobuff
- initialise messages of the SURIMI contract
	- message InitializeRequest contains time step, geography, items, and standards
		- each of which has its own .proto
	- this is message is passed by the controller to all models inform the models what messages they will be receiving
	- fail-fast system
		- needs to be integrated in the model
			- start simple by just returning true, later this can be used as a control function
		
## Risk Table for PR 1
- finalised by Jeroen and Timo 
- Risk 4 correct
- Risk 6 correct
 
