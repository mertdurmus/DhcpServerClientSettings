import { Component, OnInit } from '@angular/core';
import { DhcpLeasesServiceService } from '../services/dhcp-leases-service.service';
import { Lease } from '../models/lease';

@Component({
  selector: 'app-dhcp-leases',
  templateUrl: './dhcp-leases.component.html',
  styleUrls: ['./dhcp-leases.component.css']
})
export class DhcpLeasesComponent implements OnInit {

  leases: Lease[];

  constructor(private service: DhcpLeasesServiceService) { }

  
  ngOnInit() {

    this.service.getLeases().subscribe(data => {
      this.leases = data;
    });
    console.log(this.leases);
  }

}
