package {{ package }};

import android.os.AsyncTask;
import android.util.Log;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

public class {{ task_class_name }} extends AsyncTask<Void, Void, {{ representationModel }}[]> {
        @Override
        protected {{ representationModel }}[] doInBackground(Void... params) {
            try {	
		final String url = "{{ restUri }}{{ representationModel|lower }}";
                RestTemplate restTemplate = new RestTemplate();
                restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
                {{ representationModel }}[] {{ representationModel|lower }} = restTemplate.getForObject(url, {{ representationModel }}[].class);
                return {{ representationModel|lower }};
            } catch (Exception e) {
                Log.e("MainActivity", e.getMessage(), e);
            }

            return null;
        }

        @Override
        protected void onPostExecute({{ representationModel }}[] {{ representationModel|lower }}) {
            Log.e("onPostExecute", {{ representationModel|lower }}.toString());
        }

    }