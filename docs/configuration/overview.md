# AIS-catcher Architecture

## Usage Profiles

AIS-catcher follows a modular architecture that can scale from simple to complex configurations to cater for various use cases.

<style>
.profile-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
  max-width: 1200px;
  margin: 1rem auto;
}

.profile-card {
  border: 2px solid #ccc;
  border-radius: 0.5rem;
  padding: 0.5rem;
}

.profile-title {
  font-weight: bold;
  margin: 0 0 0.0rem 0;
}

.profile-desc {
  margin: 0;
}

@media (max-width: 768px) {
  .profile-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="profile-grid">
  <div class="profile-card">
    <div class="profile-title">Receiver</div>
    <p class="profile-desc">Minimal decode & output</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Aggregator</div>
    <p class="profile-desc">Route & filter streams</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Database</div>
    <p class="profile-desc">Log to PostgreSQL</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Experimenter</div>
    <p class="profile-desc">Multi-SDR testing</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Map Viewer</div>
    <p class="profile-desc">Built-in visualization</p>
  </div>
</div>

## Basic Data Flow

In its simplest form, AIS-catcher processes data through three main stages:


<div>
<svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <!-- Basic Flow -->
  <g transform="translate(50,50)">
    <text x="0" y="-20" font-size="16" font-weight="bold">Basic Flow</text>
    
    <!-- Boxes -->
    <rect x="0" y="0" width="100" height="50" rx="5" fill="#e3f2fd" stroke="#1976d2" stroke-width="2"/>
    <rect x="150" y="0" width="100" height="50" rx="5" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>
    <rect x="300" y="0" width="100" height="50" rx="5" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>
    
    <!-- Labels -->
    <text x="50" y="30" text-anchor="middle">Input</text>
    <text x="200" y="30" text-anchor="middle">Model</text>
    <text x="350" y="30" text-anchor="middle">Output</text>
    
    <!-- Arrows -->
    <path d="M100,25 L150,25" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>
    <path d="M250,25 L300,25" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>
  </g>
</svg>
</div>

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

<div>
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">

  <!-- Advanced Flow -->
  <g transform="translate(50,200)">
    <text x="0" y="-20" font-size="16" font-weight="bold">Advanced Architecture</text>
    
    <!-- Input 1 -->
    <rect x="0" y="0" width="100" height="50" rx="5" fill="#e3f2fd" stroke="#1976d2" stroke-width="2"/>
    <text x="50" y="30" text-anchor="middle">Input 1</text>
    
    <!-- Input 2 -->
    <rect x="0" y="100" width="100" height="50" rx="5" fill="#e3f2fd" stroke="#1976d2" stroke-width="2"/>
    <text x="50" y="130" text-anchor="middle">Input 2</text>
    
    <!-- Models -->
    <rect x="150" y="0" width="100" height="40" rx="5" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>
    <text x="200" y="25" text-anchor="middle">Model A1</text>
    
    <rect x="150" y="50" width="100" height="40" rx="5" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>
    <text x="200" y="75" text-anchor="middle">Model A2</text>
    
    <rect x="150" y="100" width="100" height="40" rx="5" fill="#fce4ec" stroke="#c2185b" stroke-width="2"/>
    <text x="200" y="125" text-anchor="middle">Model B</text>
    
    <!-- Outputs -->
    <rect x="300" y="0" width="100" height="40" rx="5" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>
    <text x="350" y="25" text-anchor="middle">Output 1</text>
    
    <rect x="300" y="50" width="100" height="40" rx="5" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>
    <text x="350" y="75" text-anchor="middle">Output 2</text>
    
    <rect x="300" y="100" width="100" height="40" rx="5" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>
    <text x="350" y="125" text-anchor="middle">Output 3</text>
    
    <!-- Arrows -->
    <defs>
      <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
        <polygon points="0 0, 10 3.5, 0 7" fill="black"/>
      </marker>
    </defs>
    
    <!-- Input 1 to Models -->
    <path d="M100,25 L150,20" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <path d="M100,25 L150,70" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    
    <!-- Input 2 to Model -->
    <path d="M100,125 L150,120" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    
    <!-- Models to Outputs -->
    <path d="M250,20 L300,20" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <path d="M250,20 L300,70" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <path d="M250,70 L300,70" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <path d="M250,70 L300,120" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <path d="M250,120 L300,70" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
    <path d="M250,120 L300,120" stroke="black" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  </g>
</svg>

</div>

In this advanced setup: Multiple input sources operate independently. Each input can use multiple specialized models for decoding.  Each model can send data to one or more multiple outputs.
