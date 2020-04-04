import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DhcpLeasesComponent } from './dhcp-leases/dhcp-leases.component';
import { DhcpLeasesServiceService } from './services/dhcp-leases-service.service';

@NgModule({
  declarations: [
    AppComponent,
    DhcpLeasesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [DhcpLeasesServiceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
