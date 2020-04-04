import { TestBed } from '@angular/core/testing';

import { DhcpLeasesServiceService } from './dhcp-leases-service.service';

describe('DhcpLeasesServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DhcpLeasesServiceService = TestBed.get(DhcpLeasesServiceService);
    expect(service).toBeTruthy();
  });
});
