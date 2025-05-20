
# SURIMI Sequence Diagram
```mermaid

 sequenceDiagram

    participant Config
    participant GUI
    participant Controller
    participant EwE
    participant Poseidon
    participant CMSY
    participant Market
    participant ValueChain

    %% Initialization %%
    %% this is the init %%
    GUI ->> Config: request config
    Config ->> GUI: config
    GUI ->> Controller: init simulation

    Controller ->> EwE: init (config)
    EwE ->> Controller: success?
    Controller ->> Poseidon: init (config)
    Controller ->> CMSY: init (config)
    Controller ->> Market: init (config)
    Controller ->> ValueChain: init (config)

    Controller ->> CMSY: create stock assessment (initial)

    %% Simulation %%
    %% starting the simulation %%
    GUI ->> Controller: run simulation

    loop N years
        loop 12 months
            Controller ->> Market: request prices
            activate Market
            Market -->> Controller: prices
            deactivate Market
            Controller ->> EwE: update prices
            Controller ->> Poseidon: update prices
            Controller ->> EwE: request biomass
            activate EwE
            EwE -->> Controller: biomass
            deactivate EwE
            Controller ->> Poseidon: update biomass
            Controller ->> CMSY: update biomass
            Controller ->> Poseidon: simulate timestep (1 month)
            Controller ->> Poseidon: request sales
            activate Poseidon
            Poseidon -->> Controller: sales
            deactivate Poseidon
            Controller ->> Poseidon: request catches
            activate Poseidon
            Poseidon -->> Controller: catches
            deactivate Poseidon
            Controller ->> EwE: update catches
            Controller ->> CMSY: update catches
            Controller ->> Poseidon: request discards
            activate Poseidon
            Note over Poseidon: discards by fleet<br/> location and species
            Poseidon ->> Controller: discards
            deactivate Poseidon
            Controller ->> EwE: update discards
            Controller ->> EwE: simulate timestep (1 month)
            Controller ->> Market: update sales
        end
    end
    Controller ->> CMSY: create stock assessment (final) 
```
