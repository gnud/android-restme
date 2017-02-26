package com.damjan_dimitrioski.resttest.rest;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Greetings {

  private String first_name;
  private String middle_name;
  private String last_name;
  
  public String getFirst_name() {
      return this.first_name;
  }

  public void setFirst_name(String first_name) {
      this.first_name = first_name;
  }
  
  public String getMiddle_name() {
      return this.middle_name;
  }

  public void setMiddle_name(String middle_name) {
      this.middle_name = middle_name;
  }
  
  public String getLast_name() {
      return this.last_name;
  }

  public void setLast_name(String last_name) {
      this.last_name = last_name;
  }
        

  @Override
  public String toString() {
    return  this.getFirst_name() +  this.getMiddle_name() +  this.getLast_name() +  "";
  }
} 