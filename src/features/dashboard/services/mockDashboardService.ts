import { mockDashboardData } from '../data/mockDashboardData';
import type { DashboardData } from '../types/dashboard';

export async function getDashboardData(): Promise<DashboardData> {
  return Promise.resolve(mockDashboardData);
}
