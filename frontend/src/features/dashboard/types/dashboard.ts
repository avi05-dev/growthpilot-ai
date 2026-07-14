import type { Priority } from '../../../theme/tokens';

export type DashboardLoadState = 'loading' | 'success' | 'empty' | 'error';

export type TrendCategory = 'AI' | 'Development' | 'Career';

export type TrendSource = 'GitHub' | 'Reddit' | 'Hacker News' | 'Dev.to' | string;

export type BriefingItem = {
  id: string;
  text: string;
};

export type DailyBriefing = {
  title: string;
  items: BriefingItem[];
  bestPostingWindow: string;
  recommendedFocus: string;
};

export type Trend = {
  id: string;
  category: TrendCategory;
  title: string;
  description: string;
  score: number;
  sources: TrendSource[];
};

export type ContentRecommendation = {
  id: string;
  channel: string;
  topic: string;
  actionLabel: string;
};

export type ActionTask = {
  id: string;
  title: string;
  description: string;
  priority: Priority;
};

export type KpiMetric = {
  id: string;
  label: string;
  value: string;
  helper: string;
};

export type DashboardData = {
  briefing: DailyBriefing;
  trends: Trend[];
  contentRecommendations: ContentRecommendation[];
  actionTasks: ActionTask[];
  kpis: KpiMetric[];
};
