package com/damjan_dimitrioski/resttest;

import android.os.AsyncTask;
import android.util.Log;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

public class GreetingsCallTask extends AsyncTask<Void, Void, greetings[]> {
        @Override
        protected greetings[] doInBackground(Void... params) {
            try {	
		final String url = "http://192.168.0.100:3004/greetings";
                RestTemplate restTemplate = new RestTemplate();
                restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
                greetings[] greetings = restTemplate.getForObject(url, greetings[].class);
                return greetings;
            } catch (Exception e) {
                Log.e("MainActivity", e.getMessage(), e);
            }

            return null;
        }

        @Override
        protected void onPostExecute(greetings[] greetings) {
            Log.e("onPostExecute", greetings.toString());
        }

    }