# AIS-catcher Architecture

AIS-catcher follows a modular architecture that can scale from simple to complex configurations. Let's explore both scenarios:

## Basic Architecture

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

Input: Single data source (e.g., an SDR device)
Model: Message decoding and processing
Output: Delivery of decoded messages (e.g., to screen)


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

In this advanced setup:
Inputs

Multiple input sources operate independently
Each input can use multiple specialized models
Examples: RTL-SDR, Airspy, network streams, files

Models

Input 1 uses two parallel models (A1 and A2)
Input 2 uses a single dedicated model (B)
Models are optimized for their specific input source

Outputs

Each model can send data to multiple outputs
Outputs can receive data from multiple models
Examples: screen display, file logging, network streaming, database storage

Configuration
Each component can be configured independently:

Input Configuration: Configure devices, files, and network sources
Model Configuration: Adjust signal processing and decoding parameters
Output Configuration: Set up various output formats and destinations

This modular architecture allows for flexible setups ranging from simple single-channel monitoring to complex multi-receiver systems with diverse output requirements.

