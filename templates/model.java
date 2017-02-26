package {{ package }};

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class {{ representationModel|capitalize }} {

  {% for field in fields -%}
  private {{ field.type }} {{ field.name }};
  {% endfor -%}

  {% for field in fields %}
  public String get{{ field.name|capitalize }}() {
      return this.{{ field.name }};
  }

  public void set{{ field.name|capitalize }}({{ field.type }} {{ field.name }}) {
      this.{{ field.name }} = {{ field.name }};
  }
  {% endfor %}      

  @Override
  public String toString() {
    return {% for field in fields %} this.get{{ field.name|capitalize }}() + {% endfor %} "";
  }
} 
