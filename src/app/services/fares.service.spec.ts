import { TestBed } from '@angular/core/testing';

import { FaresService } from './fares.service';

describe('FaresService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: FaresService = TestBed.get(FaresService);
    expect(service).toBeTruthy();
  });
});
