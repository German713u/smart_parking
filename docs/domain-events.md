# Eventos dominantes

| # | Evento | Emitter | Datos | Regla ⋂ Invariante |
|---|--------|---------|-------|--------------------|
| 1 | SpotReserved              | API REST           | spot_id, customer_id, until | No puede existir reserva si spot ocupado |
| 2 | GateEntered               | Gate HW           | license_plate, timestamp   | — |
| 3 | SessionStarted            | Core              | session_id, weather, rate  | Se emite tras GateEntered |
| 4 | PriceCalculated           | Core              | amount, breakdown          | Usa tarifa dinámica vigente |
| 5 | PaymentAuthorised         | Stripe Webhook    | payment_id, amount         | Importe ≥ PriceCalculated |
| 6 | GateExited                | Gate HW           | license_plate, timestamp   | — |
| 7 | SessionCompleted          | Core              | session_id, total_amount   | Requiere PaymentAuthorised |
