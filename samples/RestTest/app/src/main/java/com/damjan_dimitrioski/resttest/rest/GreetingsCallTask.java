package com.damjan_dimitrioski.resttest.rest;

import android.os.AsyncTask;
import android.util.Log;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;

public class GreetingsCallTask extends AsyncTask<Void, Void, Greetings[]> {
        @Override
        protected Greetings[] doInBackground(Void... params) {
            try {	
		        final String url = "http://192.168.0.100:3004/greetings";
                RestTemplate restTemplate = new RestTemplate();
                restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
                Greetings[] greetings = restTemplate.getForObject(url, Greetings[].class);
                return greetings;
            } catch (Exception e) {
                Log.e("MainActivity", e.getMessage(), e);
            }

            return null;
        }

        @Override
        protected void onPostExecute(Greetings[] greetings) {
            Log.e("onPostExecute", "");
            for(Greetings greetings1 : Arrays.asList(greetings))
                Log.e("item:", greetings1.toString());
        }

    }