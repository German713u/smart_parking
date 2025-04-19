```mermaid
flowchart LR
    subgraph External
        Weather[OpenWeatherMap<br/>(REST)]
        Geo[OpenStreetMap Nominatim<br/>(REST)]
        Stripe[Stripe<br/>(Webhook)]
        Sensors[IoT Sensors<br/>(MQTT)]
        Dashboard[Parking Dashboard<br/>(WebSocket)]
    end

    Garage[Smart Parking Garage<br/>(Core Bounded Context)]

    Weather -->|Forecast JSON| Garage
    Geo -->|Geo JSON| Garage
    Garage -->|Stripe API| Stripe
    Stripe -->|payment_succeeded| Garage
    Sensors -->|occupancy events| Garage
    Garage -->|events| Dashboard
