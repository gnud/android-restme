package {{ package }};

import android.os.AsyncTask;
import android.util.Log;
import java.util.Arrays;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

public class {{ task_class_name }} extends AsyncTask<Void, Void, {{ representationModel|capitalize }}[]> {
        @Override
        protected {{ representationModel|capitalize }}[] doInBackground(Void... params) {
            try {	
		        final String url = "{{ restUri }}{{ representationModel|lower }}";
                RestTemplate restTemplate = new RestTemplate();
                restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
                {{ representationModel|capitalize }}[] {{ representationModel|lower }} = restTemplate.getForObject(url, {{ representationModel|capitalize }}[].class);
                return {{ representationModel|lower }};
            } catch (Exception e) {
                Log.e("MainActivity", e.getMessage(), e);
            }

            return null;
        }

        @Override
        protected void onPostExecute({{ representationModel|capitalize }}[] {{ representationModel|lower }}) {
            Log.e("onPostExecute", "");
            for({{ representationModel|capitalize }} {{ representationModel|lower }}_item : Arrays.asList({{ representationModel|lower }}))
                Log.e("item:", {{ representationModel|lower }}_item.toString());
        }

    }