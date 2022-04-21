import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';

import { AppComponent } from './app.component';
import { FluxComponent } from './flux/flux.component';
import { WebAPIService } from './web-api.service';

@NgModule({
  declarations: [
    AppComponent,
    FluxComponent,

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [WebAPIService],
  bootstrap: [AppComponent]
})
export class AppModule { }
