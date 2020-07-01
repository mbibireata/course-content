def predict_spike_counts_lg(stim, spikes, d=25):
  """Compute a vector of predicted spike counts given the stimulus.

  Args:
    stim (1D array): Stimulus values at each timepoint
    spikes (1D array): Spike counts measured at each timepoint
    d (number): Number of time lags to use.

  Returns:
    yhat (1D array): Predicted spikes at each timepoint.

  """
  y = spikes
  constant = np.ones_like(y)
  X = np.column_stack([constant, make_design_matrix(stim)])
  theta = np.linalg.inv(X.T @ X) @ X.T @ y
  yhat = X @ theta
  return yhat

predicted_counts = predict_spike_counts_lg(stim, spikes)
with plt.xkcd():
  plot_spikes_with_prediction(spikes, predicted_counts, dt_stim)