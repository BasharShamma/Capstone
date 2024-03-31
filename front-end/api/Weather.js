import { fetchWeatherApi } from 'openmeteo';

const Weather = async ({ latitude, longitude }) => {
  const params = {
    latitude: latitude,
    longitude: longitude,
    current: "temperature_2m"
  };

  const url = "https://api.open-meteo.com/v1/forecast";

  try {
    const responses = await fetchWeatherApi(url, params);
    const response = responses[0];

    const utcOffsetSeconds = response.utcOffsetSeconds();
    const current = response.current();

    return {
      time: new Date((Number(current.time()) + utcOffsetSeconds) * 1000),
      temperature2m: current.variables(0).value(),
    };
    
  } catch (error) {
    console.error("Error fetching weather data:", error);
    // You might want to handle the error or return a default value here
    
  }

  return (
    <div>
      {weatherData && (
        <div>
          <p>Current Temperature:</p>
          {/* Add other weather information here */}
        </div>
      )}
    </div>
  );

};

export default Weather;
