# AIS-catcher Architecture

## Usage Profiles

AIS-catcher follows a modular architecture that can scale from simple to complex configurations to cater for various use cses.


**Receiver**

Minimal options for decoding and output 

**Aggregator** 

Route and filter streams to aggregators

**Database**

Log all messages to PostgreSQL 

**Experimenter**

Simultaneous SDRs, decoder testing

**Web Viewer**

Display vessels via built-in web interface


## Basic Data Flow

In its simplest form, AIS-catcher processes data through three main stages:

```mermaid
flowchart LR
    I[Input] -->M[Model]
    M --> O[Output]
    style I fill:#e3f2fd,stroke:#1976d2
    style M fill:#e8f5e9,stroke:#2e7d32
    style O fill:#fff3e0,stroke:#e65100
    click I "input" _blank
    click M "model" _blank
    click O "output" _blank
```

## Documentation Structure

The documentation is organized along these lines.

[***Input***](input/overview.md)  

Examples: RTL-SDR, Airspy, network streams, files.

[***Model***](model.md)  

Message decoding and processing. AIS-catcher includes various decoding models for experimentation.

[***Output***](output/overview.md)  

Examples: screen display, file logging, network streaming, database storage


## Advanced Architecture
For more complex setups, AIS-catcher supports multiple inputs with input-specific models:

```mermaid
flowchart LR
    %% Input 1 with two models
    I1[Input 1] --> M1[Model A1]
    I1 --> M2[Model A2]
    
    %% Input 2 with one model
    I2[Input 2] --> M3[Model B]
    
    %% Models to Outputs
    M1 --> O1[Output 1]
    M1 --> O2[Output 2]
    M2 --> O2
    M2 --> O3[Output 3]
    M3 --> O2
    M3 --> O3
    
    %% Styling
    style I1 fill:#e3f2fd,stroke:#1976d2
    style I2 fill:#e3f2fd,stroke:#1976d2
    style M1 fill:#e8f5e9,stroke:#2e7d32
    style M2 fill:#e8f5e9,stroke:#2e7d32
    style M3 fill:#fce4ec,stroke:#c2185b
    style O1 fill:#fff3e0,stroke:#e65100
    style O2 fill:#fff3e0,stroke:#e65100
    style O3 fill:#fff3e0,stroke:#e65100
    
    click I1 "input" _blank
    click I2 "input" _blank
    click M1 "model" _blank
    click M2 "model" _blank
    click O1 "output" _blank
    click O2 "output" _blank
    click O3 "output" _blank
```

In this advanced setup: Multiple input sources operate independently. Each input can use multiple specialized models for decoding.  Each model can send data to one or more multiple outputs.
