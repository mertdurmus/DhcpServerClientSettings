import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DhcpLeasesComponent } from './dhcp-leases/dhcp-leases.component';

const routes: Routes = [
  {path: 'leases', component: DhcpLeasesComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
