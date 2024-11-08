-- Create a model using the data from the transaction table
CREATE OR REPLACE MODEL
  `<projectname>.<datasetname>.<model_name>`
OPTIONS(
  model_type='ARIMA_PLUS',
  time_series_timestamp_col='timestamp',
  time_series_data_col='value',
  time_series_id_col=['user_id'],
  auto_arima=TRUE,
  data_frequency='AUTO_FREQUENCY')
AS SELECT
  transaction_id,        -- The internal transaction ID
  user_id,               -- The user whose credit is affected by this transaction
  timestamp AS ts,      -- Timestamp for the transaction
  value AS amount,       -- The value of this transaction
  refunded,              -- Refunded status
  notes,                 -- Extra notes on the transaction
  provider,              -- Payment provider
  telegram_charge_id,    -- Transaction ID supplied by Telegram
  provider_charge_id,    -- Transaction ID supplied by the payment provider
  payment_name,          -- Extra transaction data for disputes
  payment_phone,         -- Phone number related to the payment
  payment_email,         -- Email related to the payment
  order_id               -- Order ID
FROM
  transaction;

-- Detect anomalies using the created model
SELECT
  transaction_id,        -- The internal transaction ID
  user_id,               -- The user whose credit is affected by this transaction
  ts,                    -- Timestamp for the transaction
  amount,                -- The value of this transaction
  refunded,              -- Refunded status
  notes,                 -- Extra notes on the transaction
  provider,              -- Payment provider
  telegram_charge_id,    -- Transaction ID supplied by Telegram
  provider_charge_id,    -- Transaction ID supplied by the payment provider
  payment_name,          -- Extra transaction data for disputes
  payment_phone,         -- Phone number related to the payment
  payment_email,         -- Email related to the payment
  order_id,              -- Order ID
  lower_bound, 
  upper_bound, 
  anomaly_probability, 
  is_anomaly 
FROM
  ML.DETECT_ANOMALIES(MODEL `<projectname>.<datasetname>.<model_name>`, STRUCT(0.9 AS anomaly_prob_threshold),
  (
      SELECT
        transaction_id,        -- The internal transaction ID
        user_id,               -- The user whose credit is affected by this transaction
        timestamp AS ts,      -- Timestamp for the transaction
        value AS amount,       -- The value of this transaction
        refunded,              -- Refunded status
        notes,                 -- Extra notes on the transaction
        provider,              -- Payment provider
        telegram_charge_id,    -- Transaction ID supplied by Telegram
        provider_charge_id,    -- Transaction ID supplied by the payment provider
        payment_name,          -- Extra transaction data for disputes
        payment_phone,         -- Phone number related to the payment
        payment_email,         -- Email related to the payment
        order_id               -- Order ID
      FROM
        transaction)) 
ORDER BY ts;
