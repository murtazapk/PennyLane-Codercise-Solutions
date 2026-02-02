# I.1.3 Sampling measurement outcome
def measure_state(state,num_meas):
    probabilities=np.abs(state)**2
    samples=np.random.choice(
        a=[0,1],
        size=num_meas,
        p=probabilitees
    )
    return sample
    pass
